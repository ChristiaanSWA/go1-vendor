<template>
        
  <div>

    <LeftSidebar :isCollapsed="isSidebarCollapsed" @toggle="toggleSidebar" />
    
    <div :class="['head-layout', { collapsed: isSidebarCollapsed }]">

      <div class="head-content">
        <header class="border-b bg-white p-4 font-medium text-xl">
            Purchase Invoice Details
        </header>
      </div>

    </div>

    <div class="main-content justify-items-center grid grid-cols-1 py-10">

      
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

          <div class="mb-5 text-lg font-medium">
            <h1> Details: </h1>
          </div>

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
              <span class="text-gray-600 text-sm">Input Value</span>
              <span class="text-sm font-semibold">{{ inputValue }}</span>
            </div>


            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Total Value</span>
              <span class="text-sm font-semibold">{{ totalValue }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Due Date</span>
              <span class="text-sm font-semibold">{{ duedateValue }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Posting Time</span>
              <span class="text-sm font-semibold">{{ postingtime }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Supplier Address</span>
              <span class="text-sm font-semibold">{{ supplieraddress }}</span>
            </div>

            

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Shipping Address</span>
              <span class="text-sm font-semibold" v-html="shippingaddress"></span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Supplier</span>
              <span class="text-sm font-semibold">{{ supplier }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Supplier Address Line 1</span>
              <span class="text-sm font-semibold">{{ sup_address_line1 }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">PO Code</span>
              <span class="text-sm font-semibold">{{ pocode }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">PO Reference</span>
              <span class="text-sm font-semibold">{{ poreference }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Allowed Currency</span>
              <span class="text-sm font-semibold">{{ allowedcurrency }}</span>
            </div>

            <div class="flex flex-col gap-1">
              <span class="text-gray-600 text-sm">Address</span>
              <span class="text-sm font-semibold" v-html="address"></span>
            </div>


          </div>
         
          

          
          
        </div>

        <!-- items -->
        <div class="grid grid-cols-1">

          

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
                      <th class="p-3 text-md font-normal text-right">Rate</th>
                      <th class="p-3 text-md font-normal text-right">Amount</th>
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
                      <td class="px-3 py-2 text-right text-md font-medium">
                          <p>{{ row.rate }}</p>
                      </td>
                      <td class="px-3 py-2 text-right text-md font-medium">
                          <p>{{ row.amount }}</p>
                      </td>
                  </tr>

                  



              </tbody>

            </table>       
          </div>

        </div>

        <div class="grid grid-cols-1 p-3">

          

          <div class="grid grid-cols-1  gap-8  md:grid-cols-2">

            <div></div>

            <div class="flex flex-col w-full gap-3" >
              <div class="flex justify-between items-center"><span class="text-gray-600 text-sm font-medium">Tax Amount</span><span class="text-sm font-medium">{{ total_taxes }}</span></div>
              <div class="flex justify-between items-center"><span class="text-gray-600 text-sm font-medium">Total</span><span class="text-sm font-medium">{{ total }}</span></div>
            </div>

          </div>


          
        </div>


        <div class="grid grid-cols-1">

          
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
                      <th class="p-3 w-1/2 text-md font-normal" >Type</th>
                      <th class="p-3 text-md font-normal">Account Head</th>
                      <th class="p-3 text-md font-normal">Tax Rate</th>
                      <th class="p-3 text-md font-normal">Amount</th>
                      <th class="p-3 text-md font-normal text-right">Total</th>
                  </tr>
              </thead>

              <tbody>

                  <tr v-for="(row, index) in supplierValue" :key="index" class="border-b border-gray-200">
                      <td class="px-3 py-2 w-1/2 text-md font-medium"  >
                        <p>{{ row.charge_type }}</p>
                      </td>
                      <td class="px-3 py-2 text-center text-md font-medium">
                          <p>{{ row.account_head }}</p>
                      </td>
                      <td class="px-3 py-2 text-md font-medium">
                          <span>{{ row.rate }}</span>
                      </td>
                      <td class="px-3 py-2 text-center text-md font-medium">
                          <p>{{ row.tax_amount }}</p>
                      </td>
                      <td class="px-3 py-2 text-right text-md font-medium">
                          <p>{{ row.total }}</p>
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
import { createResource, Breadcrumbs, Button, FormControl, Badge } from 'frappe-ui'
import { useRouter, useRoute } from 'vue-router'

export default {
  components: {
    LeftSidebar,
    // Breadcrumbs,
    FormControl,
    Badge,
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
    const duedateValue = ref([])
    const postingtime = ref([])
    const supplieraddress = ref([])
    const address = ref([])
    const shippingaddress = ref([])
    const supplier = ref([])
    const sup_address_line1=ref([])
    const pocode = ref([])
    const poreference = ref([])
    const allowedcurrency = ref([])
    const total = ref('')
    const total_taxes = ref('')
    const total_advance = ref('')
    // const Paymentterms = ref("")
    const taxnumber = ref("")
    const inovice_bill_data = ref("")
  
    const quote = createResource({
      url: 'go1_vendor.api.get_purchaseinvoice',
      method: 'get',
    })

    

    // const breadcrumbsList = ref([
    //   { label: 'Quotation', route: { name: 'Request Quotation' } },
    //   { label: '', route: {} },
    // ])

    console.log('value', quote)
    const fetchQuoteDetails = async () => {
      try {
        const id = route.params.id
        const data = await quote.fetch()
        const QuotationDetails = data.find((items) => items.name === id)
        console.log('qoute,', QuotationDetails)
        if (QuotationDetails) {
          console.log('child', QuotationDetails.tax_id)
          allowedcurrency.value = QuotationDetails.price_list_currency
          taxnumber.value =QuotationDetails.tax_id || "name"  
          itemValue.value = QuotationDetails.items || []
          supplierValue.value = QuotationDetails.taxes || []
          totalValue.value = QuotationDetails.total
          inovice_bill_data.value = QuotationDetails.bill_date
          total.value = QuotationDetails.totals
          
          name.value = QuotationDetails.name
          inputValue.value = QuotationDetails.status
          datevalue.value = QuotationDetails.posting_date
          requiredate.value = QuotationDetails.schedule_date
          company.value = QuotationDetails.company
          billing_details.value = QuotationDetails.billing_address_display
          billing_address.value = QuotationDetails.billing_address
          duedateValue.value = QuotationDetails.due_date
          postingtime.value = QuotationDetails.posting_time
          supplieraddress.value = QuotationDetails.supplier_address
          address.value = QuotationDetails.address_display
          supplier.value = QuotationDetails.supplier
          shippingaddress.value = QuotationDetails.shipping_address
          pocode.value = QuotationDetails.supplier_name
          poreference.value = QuotationDetails.bill_no
          sup_address_line1.value = QuotationDetails.sup_address_line1

          total.value = QuotationDetails.total
          total_taxes.value = QuotationDetails.total_taxes_and_charges
          total_advance.value = QuotationDetails.total_advance

          console.log(QuotationDetails.total)
          console.log(QuotationDetails)
            // Paymentterms.value = QuotationDetails.payment_terms_template
          
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

    // Dynamically set border width for the status dot
    const borderWidth = computed(() => 'auto')

    const getTheme = (inputValue) => {
      if (inputValue === 'Paid') {
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

    return {
      total,
      total_taxes,
      total_advance,
      isSidebarCollapsed,
      name,
      inputValue,
      itemValue,
      totalValue,
      toggleSidebar,
      taxnumber,
      // breadcrumbsList,
      statusColor,
      statusColorText,
      statusBorColor,
      borderWidth,
      quote,
      supplierValue,
      company,
      inovice_bill_data,
      billing_address,
      billing_details,
      datevalue,
      requiredate,
      duedateValue,
      postingtime,
      supplieraddress,
      address,
      supplier,
      getTheme,
      shippingaddress,
      pocode,
      poreference,
      allowedcurrency,
      sup_address_line1
      // Paymentterms,
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
