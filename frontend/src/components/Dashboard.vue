<script setup lang="ts">
import { ref, computed } from 'vue';
import { Clock, MapPin, Users, Plus, Trash2, X } from 'lucide-vue-next';

// --- STATS DATA ---
const stats = [
  { title: 'Upcoming Events', value: '0', subtitle: 'This month' },
  { title: 'Total Attendees', value: '0', subtitle: 'Expected participants' },
  { title: 'Active HOAs', value: '0', subtitle: 'With scheduled events' },
];

// --- CALENDAR & EVENT STATE ---
interface HoaEvent {
  id: number;
  date: Date;
  title: string;
  hoa: string;
  time: string;
  location: string;
  attendees: number;
}

const currentDate = ref(new Date()); 
const selectedDate = ref<Date | null>(null); 
const events = ref<HoaEvent[]>([]);

// --- MODAL STATE ---
const isEventModalOpen = ref(false);
const selectedDateForNewEvent = ref<Date | null>(null);
const newEventForm = ref({ title: '', hoa: '', time: '', location: '', attendees: 0 });

// --- CALENDAR LOGIC ---
const currentMonthName = computed(() => currentDate.value.toLocaleString('default', { month: 'long', year: 'numeric' }));

const calendarDays = computed(() => {
  const year = currentDate.value.getFullYear();
  const month = currentDate.value.getMonth();
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const days = [];
  
  for (let i = 0; i < firstDayOfMonth; i++) days.push({ dayNumber: null, date: null });
  for (let i = 1; i <= daysInMonth; i++) days.push({ dayNumber: i, date: new Date(year, month, i) });
  
  return days;
});

// --- ACTIONS ---
const prevMonth = () => { currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1); selectedDate.value = null; };
const nextMonth = () => { currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1); selectedDate.value = null; };
const selectDay = (date: Date | null) => { if (date) selectedDate.value = date; };
const getEventsForDay = (date: Date | null) => { if (!date) return []; return events.value.filter(e => e.date.toDateString() === date.toDateString()); };

const addEventToDay = (date: Date, eventFromClick: Event) => {
  eventFromClick.stopPropagation(); 
  selectedDateForNewEvent.value = date;
  isEventModalOpen.value = true;
};

const submitEvent = () => {
  if (selectedDateForNewEvent.value) {
    events.value.push({
      id: Date.now(),
      date: selectedDateForNewEvent.value,
      title: newEventForm.value.title,
      hoa: newEventForm.value.hoa,
      time: newEventForm.value.time,
      location: newEventForm.value.location,
      attendees: newEventForm.value.attendees
    });
    isEventModalOpen.value = false;
    newEventForm.value = { title: '', hoa: '', time: '', location: '', attendees: 0 };
    selectedDate.value = selectedDateForNewEvent.value;
  }
};

const deleteEvent = (id: number) => {
  if (confirm("Are you sure you want to remove this event?")) {
    events.value = events.value.filter(e => e.id !== id);
  }
};

// --- DISPLAY LOGIC ---
const displayedEvents = computed(() => {
  if (selectedDate.value) return events.value.filter(e => e.date.toDateString() === selectedDate.value?.toDateString());
  return events.value.filter(e => e.date.getMonth() === currentDate.value.getMonth() && e.date.getFullYear() === currentDate.value.getFullYear()).sort((a, b) => a.date.getTime() - b.date.getTime());
});

const dynamicStats = computed(() => {
  const currentMonthEvents = events.value.filter(e => e.date.getMonth() === currentDate.value.getMonth() && e.date.getFullYear() === currentDate.value.getFullYear());
  const totalAttendees = currentMonthEvents.reduce((sum, event) => sum + Number(event.attendees), 0);
  const uniqueHOAs = new Set(currentMonthEvents.map(e => e.hoa)).size;

  return [
    { title: 'Upcoming Events', value: currentMonthEvents.length.toString(), subtitle: 'This month' },
    { title: 'Total Attendees', value: totalAttendees.toString(), subtitle: 'Expected participants' },
    { title: 'Active HOAs', value: uniqueHOAs.toString(), subtitle: 'With scheduled events' },
  ];
});
</script>

<template>
  <div class="flex-1 bg-white p-10 overflow-y-auto relative text-slate-800">
    
    <div class="mb-8">
      <h2 class="text-4xl font-semibold text-[#1a2b3c] tracking-tight">Dashboard</h2>
      <p class="text-[#64748b] mt-2 text-sm">Overview of scheduled events and activities</p>
    </div>

    <div class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <div class="xl:col-span-2 bg-white rounded-xl border border-gray-200 p-8">
        <h3 class="text-base font-semibold text-gray-800 mb-6">Calendar View</h3>
        
        <div class="flex justify-between items-center mb-4">
          <h4 class="text-lg font-bold text-gray-900">{{ currentMonthName }}</h4>
          <div class="flex gap-2">
            <button @click="prevMonth" class="px-5 py-2 bg-[#64748b] text-white text-sm font-medium rounded hover:bg-[#475569] transition-colors">Previous</button>
            <button @click="nextMonth" class="px-5 py-2 bg-[#64748b] text-white text-sm font-medium rounded hover:bg-[#475569] transition-colors">Next</button>
          </div>
        </div>
        
        <div class="border-l border-t border-gray-200 rounded-lg overflow-hidden mt-4">
          <div class="grid grid-cols-7 bg-[#f1f5f9]">
            <div v-for="day in ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']" :key="day" class="p-3 text-center text-xs font-semibold text-[#64748b] border-r border-b border-gray-200">
              {{ day }}
            </div>
          </div>
          
          <div class="grid grid-cols-7">
            <div 
              v-for="(dayObj, index) in calendarDays" 
              :key="index"
              @click="selectDay(dayObj.date)"
              class="min-h-[100px] p-2 relative group cursor-pointer border-r border-b border-gray-200 transition-colors"
              :class="[
                !dayObj.date ? 'bg-[#e2e8f0]/40' : 'bg-white hover:bg-gray-50',
                selectedDate && dayObj.date && selectedDate.toDateString() === dayObj.date.toDateString() ? 'ring-2 ring-inset ring-blue-500 bg-blue-50/20' : ''
              ]"
            >
              <span v-if="dayObj.dayNumber" class="text-sm text-gray-700">{{ dayObj.dayNumber }}</span>
              
              <button 
                v-if="dayObj.date"
                @click="(e) => addEventToDay(dayObj.date!, e)"
                class="absolute top-2 right-2 p-1 bg-gray-100 text-gray-500 rounded hover:bg-blue-600 hover:text-white opacity-0 group-hover:opacity-100 transition-opacity"
              >
                <Plus class="w-3.5 h-3.5" />
              </button>

              <div class="mt-1 flex flex-col gap-1">
                <div 
                  v-for="event in getEventsForDay(dayObj.date)" 
                  :key="event.id"
                  class="bg-[#3b82f6] text-white text-[11px] font-medium px-2 py-0.5 rounded shadow-sm truncate"
                >
                  Event
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <button v-if="selectedDate" @click="selectedDate = null" class="mt-4 text-sm text-blue-600 hover:underline">Clear selection</button>
      </div>

      <div class="flex flex-col gap-4">
        <div v-for="stat in dynamicStats" :key="stat.title" class="bg-white rounded-xl border border-gray-200 p-6">
          <p class="text-sm font-medium text-gray-600 mb-4">{{ stat.title }}</p>
          <h3 class="text-3xl font-bold text-gray-900">{{ stat.value }}</h3>
          <p class="text-sm text-gray-500 mt-1">{{ stat.subtitle }}</p>
        </div>
      </div>
    </div>

    <div class="mt-8 bg-white rounded-xl border border-gray-200 p-8">
      <h3 class="text-base font-semibold text-gray-800 mb-6">Scheduled Events</h3>
      
      <div v-if="displayedEvents.length === 0" class="text-center py-10 text-gray-500 border border-dashed border-gray-200 rounded-lg">
        No events scheduled. Click a date on the calendar to add one.
      </div>

      <div class="flex flex-col gap-4">
        <div v-for="event in displayedEvents" :key="event.id" class="flex flex-col md:flex-row p-5 border border-gray-200 rounded-xl hover:bg-gray-50 transition-colors group relative">
          
          <div class="flex flex-col items-center justify-start shrink-0 mr-6 w-12">
            <span class="text-sm text-gray-500 font-medium">{{ event.date.toLocaleString('default', { month: 'short' }) }}</span>
            <span class="text-2xl font-bold text-gray-900 leading-none mt-1">{{ event.date.getDate() }}</span>
          </div>

          <div class="flex-1">
            <h4 class="text-lg font-bold text-gray-900">{{ event.title }}</h4>
            <p class="text-sm text-[#64748b] mt-0.5 mb-3">{{ event.hoa }}</p>
            
            <div class="flex flex-wrap items-center gap-5 text-sm text-gray-500">
              <span class="flex items-center gap-1.5"><Clock class="w-4 h-4 text-gray-400" /> {{ event.time }}</span>
              <span class="flex items-center gap-1.5"><MapPin class="w-4 h-4 text-gray-400" /> {{ event.location }}</span>
              <span class="flex items-center gap-1.5"><Users class="w-4 h-4 text-gray-400" /> {{ event.attendees }} attendees</span>
            </div>
          </div>

          <div class="absolute top-5 right-5 flex items-center gap-4">
            <span class="px-3 py-1 border border-gray-300 rounded-full text-xs font-medium text-gray-600 bg-white">
              upcoming
            </span>
            <button @click="deleteEvent(event.id)" class="text-gray-400 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-opacity">
              <Trash2 class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="isEventModalOpen" class="fixed inset-0 bg-gray-900/50 z-50 flex items-center justify-center p-4">
      <div class="bg-white rounded-xl shadow-lg w-full max-w-md overflow-hidden border border-gray-200">
        <div class="flex items-center justify-between px-6 py-4 border-b border-gray-100">
          <h3 class="text-lg font-bold text-gray-900">Add New Event</h3>
          <button @click="isEventModalOpen = false" class="text-gray-400 hover:text-gray-600"><X class="w-5 h-5" /></button>
        </div>
        
        <form @submit.prevent="submitEvent" class="p-6 space-y-4">
          <div v-if="selectedDateForNewEvent" class="inline-block px-3 py-1 bg-[#f1f5f9] text-[#475569] text-xs font-semibold rounded-md mb-2">
            Scheduling for: {{ selectedDateForNewEvent.toLocaleDateString('default', { month: 'short', day: 'numeric', year: 'numeric' }) }}
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1.5">Event Title</label>
            <input v-model="newEventForm.title" required type="text" placeholder="e.g. HOA Orientation" class="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500">
          </div>
          
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1.5">Target HOA</label>
            <input v-model="newEventForm.hoa" required type="text" placeholder="e.g. Green Meadows Association" class="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500">
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-1.5">Time</label>
              <input v-model="newEventForm.time" required type="time" class="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-1.5">Attendees</label>
              <input v-model="newEventForm.attendees" type="number" min="0" class="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1.5">Location</label>
            <input v-model="newEventForm.location" required type="text" placeholder="e.g. Community Hall" class="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500">
          </div>

          <div class="flex justify-end gap-3 mt-8 pt-4 border-t border-gray-100">
            <button type="button" @click="isEventModalOpen = false" class="px-4 py-2 text-sm text-gray-600 font-medium hover:bg-gray-50 rounded-lg border border-transparent">Cancel</button>
            <button type="submit" class="px-4 py-2 bg-[#2563eb] text-white text-sm font-medium rounded-lg hover:bg-blue-700 shadow-sm">Save Event</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>