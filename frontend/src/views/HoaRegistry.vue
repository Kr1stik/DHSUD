<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Building2, Search, Edit2, Trash2, X } from 'lucide-vue-next';

interface HoaProfile {
  id?: number;
  name: string;
  registration_type: string;
  barangay: string;
  city_municipality: string;
  province: string;
  contact_person: string;
  contact_details: string;
  total_members: number;
  status: string;
}

const hoas = ref<HoaProfile[]>([]);
const isLoading = ref(true);
const isModalOpen = ref(false);

const newHoa = ref<HoaProfile>({
  name: '', registration_type: 'Regular', barangay: '', city_municipality: '', province: '', contact_person: '', contact_details: '', total_members: 0, status: 'Pending'
});

const fetchHoas = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/hoas/');
    if (!response.ok) throw new Error('Network response was not ok');
    hoas.value = await response.json();
  } catch (error) {
    console.error('Error fetching HOAs:', error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => fetchHoas());

const getStatusColor = (status: string) => {
  switch (status) {
    case 'Active': return 'bg-emerald-50 text-emerald-700 border-emerald-200/60 shadow-sm';
    case 'Suspended': return 'bg-amber-50 text-amber-700 border-amber-200/60 shadow-sm';
    case 'Revoked': return 'bg-rose-50 text-rose-700 border-rose-200/60 shadow-sm';
    case 'Pending': return 'bg-blue-50 text-blue-700 border-blue-200/60 shadow-sm';
    default: return 'bg-slate-50 text-slate-700 border-slate-200/60 shadow-sm';
  }
};

const submitForm = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/hoas/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newHoa.value),
    });

    if (response.ok) {
      isModalOpen.value = false;
      fetchHoas(); 
      newHoa.value = { name: '', registration_type: 'Regular', barangay: '', city_municipality: '', province: '', contact_person: '', contact_details: '', total_members: 0, status: 'Pending' };
    } else {
      console.error('Validation errors:', await response.json());
    }
  } catch (error) {
    console.error('Error saving HOA:', error);
  }
};
</script>

<template>
  <div class="flex-1 bg-[#f8fafc] p-8 overflow-y-auto relative">
    
    <div class="mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <h2 class="text-3xl font-bold text-slate-800 tracking-tight">HOA Management</h2>
        <p class="text-slate-500 mt-1">Manage HOA profiles and registrations</p>
      </div>
      <button @click="isModalOpen = true" class="px-5 py-2.5 bg-blue-600 text-white rounded-xl hover:bg-blue-700 font-semibold flex items-center gap-2 shadow-md shadow-blue-500/30 hover:shadow-lg hover:shadow-blue-500/40 transform hover:-translate-y-0.5 transition-all">
        <Building2 class="w-5 h-5" /> Add HOA Applicant
      </button>
    </div>

    <div class="bg-white rounded-3xl shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 overflow-hidden">
      
      <div class="p-5 border-b border-slate-100 flex items-center justify-between bg-white">
        <div class="relative w-80">
          <Search class="w-5 h-5 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input type="text" placeholder="Search HOA Name..." class="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all font-medium">
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-slate-50/80 text-slate-500 text-xs font-bold uppercase tracking-wider border-b border-slate-100">
              <th class="px-6 py-5">HOA Name</th>
              <th class="px-6 py-5">Location</th>
              <th class="px-6 py-5">Contact Person</th>
              <th class="px-6 py-5">Members</th>
              <th class="px-6 py-5">Status</th>
              <th class="px-6 py-5 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr v-if="isLoading">
              <td colspan="6" class="px-6 py-12 text-center text-slate-400 font-medium">Loading HOA data...</td>
            </tr>
            <tr v-else-if="hoas.length === 0">
              <td colspan="6" class="px-6 py-12 text-center text-slate-400 font-medium">No HOAs found in SQLite. Click "Add HOA Applicant" to start!</td>
            </tr>
            <tr v-else v-for="hoa in hoas" :key="hoa.id" class="hover:bg-slate-50/80 transition-colors group cursor-pointer">
              <td class="px-6 py-5"><p class="font-bold text-slate-800">{{ hoa.name }}</p></td>
              <td class="px-6 py-5 text-sm font-medium text-slate-600">{{ hoa.city_municipality }}, {{ hoa.province }}</td>
              <td class="px-6 py-5 text-sm font-medium text-slate-600">{{ hoa.contact_person }}</td>
              <td class="px-6 py-5 text-sm font-medium text-slate-600">{{ hoa.total_members }}</td>
              <td class="px-6 py-5">
                <span class="px-3 py-1.5 rounded-lg text-xs font-bold border" :class="getStatusColor(hoa.status)">
                  {{ hoa.status }}
                </span>
              </td>
              <td class="px-6 py-5 text-right">
                <div class="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                  <button class="p-2 text-slate-400 hover:text-blue-600 rounded-lg hover:bg-blue-50 transition-colors"><Edit2 class="w-4 h-4" /></button>
                  <button class="p-2 text-slate-400 hover:text-red-600 rounded-lg hover:bg-red-50 transition-colors"><Trash2 class="w-4 h-4" /></button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-if="isModalOpen" class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
      <div class="bg-white rounded-3xl shadow-2xl w-full max-w-3xl max-h-[90vh] overflow-y-auto border border-white/20 transform transition-all">
        <div class="sticky top-0 z-10 flex items-center justify-between px-8 py-6 border-b border-slate-100 bg-white/80 backdrop-blur-md">
          <h3 class="text-xl font-bold text-slate-800">Add New HOA Applicant</h3>
          <button @click="isModalOpen = false" class="p-2 text-slate-400 hover:text-slate-700 hover:bg-slate-100 rounded-full transition-colors"><X class="w-5 h-5" /></button>
        </div>
        
        <form @submit.prevent="submitForm" class="p-8 space-y-6">
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">HOA Name <span class="text-rose-500">*</span></label>
              <input v-model="newHoa.name" required type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none">
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Registration Type <span class="text-rose-500">*</span></label>
              <input v-model="newHoa.registration_type" required type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none">
            </div>
          </div>

          <div class="p-5 bg-slate-50/50 rounded-2xl border border-slate-100 space-y-5">
            <h4 class="text-sm font-bold text-slate-800 uppercase tracking-wider">Location Details</h4>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
              <div>
                <label class="block text-sm font-bold text-slate-700 mb-2">Province</label>
                <input v-model="newHoa.province" required type="text" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none shadow-sm">
              </div>
              <div>
                <label class="block text-sm font-bold text-slate-700 mb-2">City/Municipality</label>
                <input v-model="newHoa.city_municipality" required type="text" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none shadow-sm">
              </div>
              <div>
                <label class="block text-sm font-bold text-slate-700 mb-2">Barangay</label>
                <input v-model="newHoa.barangay" required type="text" class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none shadow-sm">
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Contact Person <span class="text-rose-500">*</span></label>
              <input v-model="newHoa.contact_person" required type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none">
            </div>
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Contact Details <span class="text-rose-500">*</span></label>
              <input v-model="newHoa.contact_details" required type="text" class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all outline-none">
            </div>
          </div>

          <div class="flex justify-end gap-3 mt-8 pt-6 border-t border-slate-100">
            <button type="button" @click="isModalOpen = false" class="px-5 py-2.5 text-slate-600 font-semibold hover:bg-slate-100 rounded-xl transition-colors">Cancel</button>
            <button type="submit" class="px-5 py-2.5 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 shadow-md shadow-blue-500/30 hover:shadow-lg hover:shadow-blue-500/40 transform hover:-translate-y-0.5 transition-all">Save Applicant</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>