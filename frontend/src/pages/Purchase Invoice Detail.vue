<template>
    <div class="p-5">
      <!-- <div :class="['head-layout', { collapsed: isSidebarCollapsed }]">
        <div class="head-content">
          <header class="border-b bg-white px-5 py-6.5 pb-[2.625rem] sm:px-5 mb-12"> -->
            <!-- <Breadcrumbs :items="breadcrumbsList" class="float-left" /> -->
            <!-- <Button
              :variant="'solid'"
              theme="gray"
              size="sm"
              label="Button"
              :loading="false"
              :loadingText="null"
              :disabled="false"
              :link="null"
              class="float-right"
            >
              + Request for Quotation
            </Button>
          </header>
        </div>
      </div> -->
      <div>
      <div class="main-content">
        <div
            class="flex items-center gap-2 leading-5 first:mt-3 grid grid-cols-1 lg:grid-cols-2 gap-4 mt-4"
          >
            <div class="shadow rounded-md p-5 min-h-72">
              <div class="text-gray-700 mb-5 ml-2 flex h-7 max-w-fit cursor-pointer items-center gap-2 pl-2 pr-3 text-base font-semibold leading-5">Details:</div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-1 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  PO Code:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center text-base text-center"
                >
                  {{ pocode }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-1 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  PO Reference:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center text-base text-center"
                >
                  {{ poreference }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-1 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Supplier:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center text-base text-center"
                >
                  {{ supplier }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Status:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ inputValue }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Date:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ datevalue }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                 Posting Time:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ postingtime }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Due Date:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ duedateValue }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Address:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  <p v-html="address"></p> 
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Supplier Address:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ supplieraddress }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Shipping Address:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ shippingaddress }}
                </div>
              </div>
            </div>
            <div class="shadow rounded-md p-5 min-h-72">
              <div class="text-gray-700 mb-5 ml-2 flex h-7 max-w-fit cursor-pointer items-center gap-2 pl-2 pr-3 text-base font-semibold leading-5">Address&Contact:</div>
              
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Address:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  <p v-html="address"></p> 
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                  Allowed Currency:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ allowedcurrency }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                   Company:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ company }}
                </div>
              </div>
              <div
                class="flex items-center gap-2 px-3 leading-5 first:mt-3 text-center mt-3 border-b pb-1"
              >
                <div class="sm: w-36 shrink-0 text-sm text-gray-600 text-left">
                   Invoice Date:
                </div>
                <div
                  class="grid min-h-[18px] flex-1 items-center overflow-hidden text-base text-center"
                >
                  {{ invoicedate }}
                </div>
              </div>
            </div>
          </div>
      </div>
      </div>
 
      <div :class="['layout', { collapsed: isSidebarCollapsed }]">
        <LeftSidebar :isCollapsed="isSidebarCollapsed" @toggle="toggleSidebar" />
        <div class="main-content">
          <div class="bg-white shadow-md rounded-lg p-6 space-y-6">
            <!-- Section 1: Form Title -->
            <div class="border-b pb-4">
              <h1 class="text-2xl font-bold text-gray-800 float-left">
                {{ name }}
              </h1>
              <Button
                :variant="'solid'"
                theme="gray"
                size="sm"
                label="Action"
                :disabled="false"
                class="float-right mb-4"
              />
              <div class="flex justify-end space-x-4 pt-4"></div>
            </div>
            <div :class="['flex items-center space-x-2 space-y-2 rounded-md p-2', statusBorColor]">
              <div :style="{ backgroundColor: statusColor, borderColor: borderColor, borderWidth: borderWidth, borderStyle: 'solid' }" class="status-dot"></div>
              <span :class="statusColorText">{{ inputValue }}</span>
            </div>
           
            <table class="min-w-full divide-y divide-gray-200">
              <thead>
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Series</th>
                  <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Company</th>
                  <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                  <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="(row, index) in itemValue" :key="index">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ row.item_code }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center">{{ row.item_name }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-right">{{ row.schedule_date }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-right">{{ row.qty }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="main-content">
          <div class="bg-white shadow-md rounded-lg p-6 ">
            <!-- Section 1: Form Title -->
            <div class="border-b pb-4">
              <h1 class="text-2xl font-bold text-gray-800 float-left">
                {{ name }}
              </h1>
              <Button
                :variant="'solid'"
                theme="gray"
                size="sm"
                label="Action"
                :disabled="false"
                class="float-right mb-4"
              />
              <div class="flex justify-end space-x-4 pt-4"></div>
            </div>
            <div :class="['flex items-center space-x-4 rounded-md p-2 ', statusBorColor]">
              <div :style="{ backgroundColor: statusColor, borderColor: borderColor, borderWidth: borderWidth, borderStyle: 'solid' }" class="status-dot"></div>
              <span :class="statusColorText">{{ inputValue }}</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            </div>
            <table class="min-w-full divide-y divide-gray-200">
              <thead>
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Account</th>
                  <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                  <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Rate</th>
                  <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Tax Amount</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="(row, index) in supplierValue" :key="index">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ row.account_head }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center">{{ row.charge_type }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-right">{{ row.rate }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-right">{{ row.tax_amount }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
  </template>
  
  <script>
  import LeftSidebar from '@/components/Custom Layout/LeftSidebar.vue'
  import { ref, watch, onMounted, computed } from 'vue'
  import { createResource, Breadcrumbs, Button,FormControl } from 'frappe-ui'
  import { useRouter, useRoute } from 'vue-router'
  
  export default {
    components: {
      LeftSidebar,
      // Breadcrumbs,
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
      const duedateValue =ref([])
      const postingtime = ref([])
      const supplieraddress = ref([])
      const address=ref([])
      const shippingaddress = ref([])
      const supplier=ref([])
      const pocode = ref([])
      const poreference = ref([])
      const allowedcurrency=ref([])
      const invoicedate=ref([])
      const quote = createResource({
        url: 'go1_vendor.sales.get_purchaseinvoice',
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
            name.value = QuotationDetails.name
            inputValue.value = QuotationDetails.status
            datevalue.value =   QuotationDetails.posting_date
            requiredate.value =   QuotationDetails.schedule_date
            company.value=QuotationDetails.company
            billing_details.value=QuotationDetails.billing_address_display
            billing_address.value=QuotationDetails.billing_address
            duedateValue.value=QuotationDetails.due_date
            postingtime.value=QuotationDetails.posting_time
            supplieraddress.value=QuotationDetails.supplier_address
            address.value=QuotationDetails.address_display
            supplier.value=QuotationDetails.supplier
            shippingaddress.value=QuotationDetails.shipping_address
            pocode.value=QuotationDetails.name
            poreference.value=QuotationDetails.bill.no
            allowedcurrency.value=QuotationDetails.currency
            invoicedate.value=QuotationDetails.bill_date

            itemValue.value = QuotationDetails.items || []
            supplierValue.value = QuotationDetails.taxes || []
            totalValue.value = QuotationDetails.total
          }
          console.log('quote1', QuotationDetails)
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
        borderWidth,
        quote,
        supplierValue,
        company,
        billing_address,
        billing_details,
        datevalue,
        requiredate,
        duedateValue,
        postingtime,
        supplieraddress,
        address,
        supplier,
        shippingaddress,
        pocode,
        poreference,
        allowedcurrency,
        invoicedate
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
  