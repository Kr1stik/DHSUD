<script setup lang="ts">
import { 
  LayoutDashboard, 
  Building2, 
  Scale, 
  AlertTriangle, 
  Ban, 
  FileText, 
  Gavel, 
  CheckCircle 
} from 'lucide-vue-next';
</script>

<template>
  <aside class="w-64 h-screen bg-[#1b2b42] text-white flex flex-col justify-between overflow-y-auto">
    
    <div>
      <div class="p-6">
        <h1 class="text-xl font-bold tracking-wide">HOA Registry</h1>
        <p class="text-xs text-blue-200 mt-1">Monitoring System</p>
      </div>

      <nav class="mt-2 flex flex-col gap-1 px-3">
        <router-link 
          to="/" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg font-medium transition-colors text-gray-300 hover:bg-[#263c5a]"
          exact-active-class="!bg-[#263c5a] !text-white"
        >
          <LayoutDashboard class="w-5 h-5" :class="$route.path === '/' ? 'text-blue-300' : 'text-gray-400'" />
          Dashboard
        </router-link>
        
        <router-link 
          to="/hoa-management" 
          class="flex items-center gap-3 px-4 py-3 rounded-lg transition-colors text-gray-300 hover:bg-[#263c5a]"
          active-class="!bg-[#263c5a] !text-white font-medium"
        >
          <Building2 class="w-5 h-5" :class="$route.path.includes('/hoa-management') ? 'text-blue-300' : 'text-gray-400'" />
          HOA Management
        </router-link>

        <div class="mt-6 mb-2 px-4">
          <p class="text-xs font-semibold text-gray-400 uppercase tracking-wider flex items-center gap-2">
            <Scale class="w-4 h-4" /> Legal Workflow
          </p>
        </div>
        
        <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-300 hover:bg-[#263c5a] rounded-lg transition-colors">
          <AlertTriangle class="w-4 h-4 text-gray-400" /> Notice of Violation
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-300 hover:bg-[#263c5a] rounded-lg transition-colors">
          <Ban class="w-4 h-4 text-gray-400" /> Order of Termination
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-300 hover:bg-[#263c5a] rounded-lg transition-colors">
          <FileText class="w-4 h-4 text-gray-400" /> Order of Imposition
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-300 hover:bg-[#263c5a] rounded-lg transition-colors">
          <Gavel class="w-4 h-4 text-gray-400" /> Motion for Reconsideration
        </a>
        <a href="#" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-300 hover:bg-[#263c5a] rounded-lg transition-colors">
          <CheckCircle class="w-4 h-4 text-gray-400" /> Compliance Status
        </a>
      </nav>
    </div>

    <div class="p-4 border-t border-[#263c5a]">
      <p class="text-[10px] text-gray-400 leading-tight">
        Government HOA Registration<br>
        Monitoring System v1.0
      </p>
    </div>
  </aside>
</template>