<template>
        
  <div>

    <LeftSidebar :isCollapsed="isSidebarCollapsed" @toggle="toggleSidebar" />
    
    <div :class="['head-layout', { collapsed: isSidebarCollapsed }]">

      <div class="head-content">
        <header class="border-b bg-white p-4 font-medium text-xl">
            Request Quotation Details
        </header>
      </div>

    </div>

    <div class="main-content justify-items-center grid grid-cols-1 py-10 h-[550px]">

      
      <div class="grid grid-cols-1 content-start gap-3 m-2 w-8/12 bg-white border rounded-md pb-5">

        <!-- heading -->
        <div class="px-3 py-3 border-b">

          <div class="flex  justify-between items-center">
              <span class="text-xl text-cyan-600 font-semibold">
                {{ name }} 
              </span>

              <Badge :variant="'subtle'" :theme="getTheme(inputValue)" size="md" label="Badge">
                {{ inputValue }}
              </Badge>
          </div>

        </div>
      
        <!-- details -->
        <div class="grid grid-cols-1 p-3">

          

          <div class="grid grid-cols-2 md:grid-cols-3 gap-3 justify-items-stretch text-gray-800">

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Name</span>
              <span class="text-sm font-semibold">{{ name }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Date</span>
              <span class="text-sm font-semibold">{{ datevalue }}</span>
            </div>

            

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Company</span>
              <span class="text-sm font-semibold">{{ company }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Billing Details</span>
              <span class="text-sm font-semibold" v-html="billing_details"></span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Billing Address</span>
              <span class="text-sm font-semibold">{{ billing_address }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Status</span>
              <span class="text-sm font-semibold">{{ inputValue }}</span>
            </div>
            
          </div>
          
        </div>

        <!-- supplier -->
        <div class="grid grid-cols-1 p-3" v-if="supplierValue[0]">

        
          <div class="grid grid-cols-2 md:grid-cols-3 gap-3 justify-items-stretch text-gray-800">

            

            

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Supplier</span>
              <span class="text-sm font-semibold">{{ supplierValue[0].supplier }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Contact</span>
              <span class="text-sm font-semibold">{{ supplierValue[0].contact }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Quote Status</span>
              <span class="text-sm font-semibold">{{ supplierValue[0].quote_status }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Supplier Name</span>
              <span class="text-sm font-semibold">{{ supplierValue[0].supplier_name }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Email ID</span>
              <span class="text-sm font-semibold">{{ supplierValue[0].email_id }}</span>
            </div>

          
            


          </div>

        </div>

        <!-- items -->
        <div class="grid grid-cols-1 ">

      

          <div class="w-full">            
            <table class="w-full text-xs text-left whitespace-nowrap">
              <colgroup>
                  <col>
                  <col>
                  <col>
                  <col>
                  <col>
              </colgroup>

              <thead>
                  <tr class="bg-gray-100">
                      <th class="p-3 w-1/2 text-md font-normal" >Item code</th>
                      <th class="p-3 text-md font-normal">Quantity</th>
                      <th class="p-3 text-md font-normal">UOM</th>
                      <th class="p-3 text-md font-normal text-center">Warehouse</th>
                      <th class="p-3 text-md font-normal text-right">Date</th>
                  </tr>
              </thead>

              <tbody>

                  <tr v-for="(row, index) in itemValue" :key="index" class="border-b border-gray-200">
                      <td class="px-3 py-2 w-1/2 text-md font-medium"  >
                        <p>{{ row.item_code }}</p>
                      </td>
                      <td class="px-3 py-2 text-center text-md font-medium">
                          <p>{{ row.qty }}</p>
                      </td>
                      <td class="px-3 py-2 text-md font-medium">
                          <span>{{ row.uom }}</span>
                      </td>
                      <td class="px-3 py-2 text-center text-md font-medium">
                          <p>{{ row.warehouse }}</p>
                      </td>
                      <td class="px-3 py-2 text-right text-md font-medium">
                          <p>{{ row.schedule_date }}</p>
                      </td>
                  </tr>

                  



              </tbody>

            </table>       
          </div>
        
        </div>
    

      </div>

    </div>
  </div>

</template>
  
  <script>
  import LeftSidebar from '@/components/Custom Layout/LeftSidebar.vue'
  import { ref, watch, onMounted, computed } from 'vue'
  import { createResource, Breadcrumbs, Button,FormControl,Badge } from 'frappe-ui'
  import { useRouter, useRoute } from 'vue-router'
  
  export default {
    components: {
      LeftSidebar,
      // Breadcrumbs,
      Badge,
      FormControl,
      Button,
    },
    setup() {
      const router = useRouter()
      const route = useRoute()
  
      const isSidebarCollapsed = ref(false)
      const name = ref('')
      const datevalue = ref('')
      const requiredate = ref('')
      const company = ref('')
      const billing_details = ref('')
      const billing_address = ref('')
      const inputValue = ref('')
      const itemValue = ref([])
      const totalValue = ref([])
      const supplierValue = ref([])
      const total = ref('') 
      const total_taxes = ref('')
      const total_advance = ref('')
      const quote = createResource({
        url: 'go1_vendor.sales.get_requestquotation',
        method: 'get',
      })

  
      // const breadcrumbsList = ref([
      //   { label: 'Quotation', route: { name: 'Request Quotation' } },
      //   { label: '', route: {} },
      // ])
     
  
      const fetchQuoteDetails = async () => {
        try {
          const id = route.params.id
          const data = await quote.fetch()
          const QuotationDetails = data.find((items) => items.name === id)
          if (QuotationDetails) {
            itemValue.value = QuotationDetails.items || []
            supplierValue.value = QuotationDetails.suppliers || []
            totalValue.value = QuotationDetails.total
            name.value = QuotationDetails.name
            inputValue.value = QuotationDetails.status
            datevalue.value =   QuotationDetails.transaction_date
            requiredate.value =   QuotationDetails.schedule_date
            company.value=QuotationDetails.company
            billing_details.value=QuotationDetails.billing_address_display
            
          }
         
        } catch (error) {
          console.error('Error fetching order details:', error)
        }
      }  
      const toggleSidebar = () => {
        isSidebarCollapsed.value = !isSidebarCollapsed.value
      }
  
      // watch(name, (newName) => {
      //   breadcrumbsList.value[1].label = newName
      // })
  
      onMounted(() => {
        fetchQuoteDetails()
      })
  
      // Computed properties to determine the status color
      const statusColor = computed(() => {
        switch (inputValue.value.toLowerCase()) {
          case 'draft':
            return 'red'
          case 'ordered':
            return 'green'
          case 'partially ordered':
            return 'yellow'
          case 'lost':
            return 'red'
          case 'cancelled':
            return 'red'
          case 'expired':
            return 'gray'
          default:
            return 'gray'
        }
      })
  
      const statusColorText = computed(() => {
        switch (inputValue.value.toLowerCase()) {
          case 'draft':
            return 'text-red-700'
          case 'ordered':
            return 'text-green-700'
          case 'partially ordered':
            return 'text-yellow-700'
          case 'lost':
            return 'text-red-700'
          case 'cancelled':
            return 'text-red-700'
          case 'expired':
            return 'text-gray-700'
          default:
            return 'text-gray-700'
        }
      })
  
      const statusBorColor = computed(() => {
        switch (inputValue.value.toLowerCase()) {
          case 'draft':
            return 'border-red-400'
          case 'ordered':
            return 'border-green-400'
          case 'partially ordered':
            return 'border-yellow-400'
          case 'lost':
            return 'border-red-400'
          case 'cancelled':
            return 'border-red-600'
          case 'expired':
            return 'border-gray-600'
          default:
            return 'border-gray-300'
        }
      })


      const getTheme = (inputValue) => {
      if (inputValue === 'Cancelled') {
        return 'green';
      } else if (inputValue === 'Completed') {
        return 'blue';
      } else if (inputValue === 'Draft') {
        return 'red';
      } else if (inputValue === 'Closed') {
        return 'orange';
      } else {
        return 'gray';
      }
    }
  
      // Dynamically set border width for the status dot
      const borderWidth = computed(() => 'auto')
  
      return {
        isSidebarCollapsed,
        name,
        inputValue,
        itemValue,
        totalValue,
        toggleSidebar,
        // breadcrumbsList,
        statusColor,
        statusColorText,
        statusBorColor,
        getTheme,
        borderWidth,
        quote,
        supplierValue,
        company,
        billing_details,
        datevalue,
        requiredate,
      }
    },
  }
  </script>
  
  <style scoped>
  .head-layout {
    display: flex;
    width: 100%;
    transition: margin-left 0.3s ease;
  }
  .layout {
    display: flex;
    width: 100%;
   
    transition: margin-left 0.3s ease;
  }
  
  .main-content {
    flex-grow: 1;
    /* padding: 1.25rem; */
    transition: margin-left 0.3s ease;
    margin-left: 220px; /* Default width of sidebar */
    

  }
  .head-content {
    flex-grow: 1;
    padding: 0px;
    transition: margin-left 0.3s ease;
    margin-left: 220px; /* Default width of sidebar */
  }
  .collapsed .main-content {
    margin-left: 60px; /* Adjust when sidebar is collapsed */
  }
  .collapsed .head-content {
    margin-left: 60px; /* Adjust when sidebar is collapsed */
  }
  .status-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border-width: var(--border-width, 2px); /* Use dynamic border width */
  }
  </style>
  