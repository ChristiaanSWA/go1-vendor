<template>
  <div :class="['sidebar', { 'collapsed': isCollapsed }]">
    <Popover v-model="isPopoverActive">
      <template #target="{ togglePopover }">
        <Button 
          @click="togglePopover" 
          :class="['flex h-12 items-center rounded-md py-2 duration-300 ease-in-out w-52 px-2 hover:bg-gray-200', { 'active': isPopoverActive }]">
          <template v-if="isCollapsed">
            <Avatar
              class="flex-shrink-0 rounded"
              :shape="'square'"
              image="http://192.168.0.156:8008/assets/erpnext/images/erpnext-logo.svg"
              label="EY"
              size="8"
            />
          </template>
          <template v-else>
            <div style="margin-left:26px">
              <div class="flex-shrink-0 text-sm duration-300 ease-in-out mr-1 ml-0 w-auto opacity-100" style="float:left;">
                <Avatar
                  class="size-8 flex-shrink-0 rounded"
                  :shape="'square'"
                  image="http://192.168.0.156:8008/assets/erpnext/images/erpnext-logo.svg"
                  label="EY"
                  size="md"
                  style="margin-left:-61px"
                />
              </div>
              <div class="flex flex-1 flex-col text-left duration-300 ease-in-out ml-2 w-auto opacity-100" style="float:left;margin-top:-2px">
                <p class="font-medium" style="margin-left:-15px">Go1 Vendor</p>
                <p style="margin-left:-15px;">{{  logged_users.data }}</p>

              </div>
              <div style="float:left;margin-left:30px;margin-top:5px" class="duration-300 ease-in-out ml-2 w-auto opacity-100">
                <FeatherIcon class="w-4" name="chevron-down" />
              </div>
            </div>
          </template>
        </Button>
      </template>
      <template #body-main>
        <div class="p-1.5">
          <Button 
            @click="sessionCheck" 
            style="text-align:left; background:white"
            class="navigation-button">
            <template v-if="isCollapsed">
              <FeatherIcon class="w-4" name="log-out" />
            </template>
            <template v-else>
              <span style="float:left"><FeatherIcon class="w-4" name="log-out" /></span>
              <span style="float:left">Logout</span>
            </template>
          </Button>
        </div>
      </template>
    </Popover>
    <div v-if="dynamicsApp.data && dynamicsApp.data.length">
      <div v-for="(row, index) in dynamicsApp.data" :key="index">
  <Button 
    @click="handleButtonClick(row.title, row.route)" 
    :variant="'ghost'"
    theme="gray"
    :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton(row.route) }]">
    <template v-if="isCollapsed">
      <FeatherIcon class="w-4" :name="row.icon"/>
    </template>
    <template v-else>
      <div class="flex w-full items-center space-x-2">
        <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" :name="row.icon"/></div>
        <div class="flex-shrink-0 text-sm duration-300 ease-in-out ml-2 w-auto opacity-100" style="float:left;">{{ row.title }}</div>
      </div>
    </template>
  </Button>
</div>
</div>

    <!-- Navigation Buttons -->
    <!-- <Button 
      @click="handleButtonClick('quotations','/Quotations')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Quotations') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="book"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="book"/></div>
          <div class="flex-shrink-0 text-sm duration-300 ease-in-out ml-2 w-auto opacity-100" style="float:left;">Quotations</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('orders','/Orders')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Orders') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="shopping-cart"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="shopping-cart"/></div>
          <div class="flex-shrink-0 text-sm duration-300 ease-in-out ml-2 w-auto opacity-100" style="float:left;">Orders</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('invoices','/Invoices')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Invoices') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="file"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="file"/></div>
          <div style="float:left;margin-left:10px">Invoices</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('shipments','/Shipments')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Shipments') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="package"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="package"/></div>
          <div style="float:left;margin-left:10px">Shipments</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('issues','/Issues')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Issues') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="help-circle"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="help-circle"/></div>
          <div style="float:left;margin-left:10px">Issues</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('addresses','/Addresses')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Addresses') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="home"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="home"/></div>
          <div style="float:left;margin-left:10px">Addresses</div>
        </div>
      </template>
    </Button>

    <Button 
      @click="handleButtonClick('material_request','/Material Request')" 
      :variant="'ghost'"
      theme="gray"
      :class="['navigation-button flex items-center rounded px-2 py-1 text-gray-800 transition hover:bg-gray-100 mt-0.5', { 'active': isActiveButton('/Material Request') }]">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="file-text"/>
      </template>
      <template v-else>
        <div class="flex w-full items-center space-x-2">
          <div style="float:left"><FeatherIcon class="w-4 text-gray-500" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-width="2" name="file-text"/></div>
          <div style="float:left;margin-left:10px">Material Request</div>
        </div>
      </template>
    </Button> -->

    <!-- Toggle Sidebar Button -->
    <Button @click="$emit('toggle')" class="toggle-button-2">
      <template v-if="isCollapsed">
        <FeatherIcon class="w-4" name="log-in" />
      </template>
      <template v-else>
        <span style="float:left"><FeatherIcon class="w-4" /></span>
        <span style="float:left">Collapse</span>
      </template>
    </Button>
  </div>
</template>

<script>
import {  ref } from 'vue'; 
import { Popover, Button, FeatherIcon, Avatar, createResource } from 'frappe-ui';
import { useRoute, useRouter } from 'vue-router'; 
import { session } from '@/data/session';
console.log("EEEEEEEE",session)
export default {
  components: {
    Popover,
    Button,
    FeatherIcon,
    Avatar,
  },
  props: {
    isCollapsed: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      isPopoverActive: false,
      session, 
      activeButton: null ,
      rows: [] 
    };
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const rows = ref([]); 
    const username =ref(['loading']);
    

    const users = createResource({
      url: 'go1_vendor.sales.get_username',
      cache:['true']
    });
    const session_users=users;
    const logged_users=session_users;
    const dynamicsApp = createResource({
    url: 'go1_vendor.sales.get_navbar_routes',
    cache: ['route','title'],
    auto: true 
  }); 
   
    const isActiveButton = (routePath) => {
      return route.path === routePath;
    };

    return {
      isActiveButton, 
      rows,
      logged_users,
      dynamicsApp
    };
  },
  methods: {
    handleButtonClick(buttonName, routePath) {
      this.setActiveButton(buttonName); 
      if (routePath) {
        this.$router.push(routePath); 
      }
    },
   
    sessionCheck() {
      session.logout.submit(); 
    },
   
    setActiveButton(button) {
      this.activeButton = button;
    },
  }
};
</script>



<style scoped>
.sidebar {
  width: 220px;
  background-color: rgb(248 248 248);
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.1);
  padding: 10px;
  transition: width 0.3s ease;
}

.collapsed {
  width: 60px;
}

.navigation-button {
  display: block;
  width: 100%;
  text-align: left;
  padding-left: .5rem;
  padding-right: .5rem;
}

.navigation-button .active{
  background-color: white;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); 
  margin-top: 0.125rem; 
  transition: all 0.2s ease-in-out;
  color: #2d3748;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1); 
}

.toggle-button-1 {
  position: absolute;
  bottom: 50px;
  left: 0;
  width: 100%;
  text-align: left;
}

.toggle-button-2 {
  position: absolute;
  bottom: 20px;
  left: 0;
  width: 100%;
  text-align: left;
}

button.active {
  background-color: white;
  /* box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); 
  margin-top: 0.125rem; 
  transition: all 0.2s ease-in-out;
  color: #2d3748;
  border-radius: 0.25rem; 
  align-items: center;
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  display:block; */
  align-items: center; 
  border-radius: 0.25rem; 
  padding-left: 0.5rem; 
  padding-right: 0.5rem; 
  padding-top: 0.25rem; 
  padding-bottom: 0.25rem; 
  color: #4a5568; 
  transition: all 0.2s ease;
  background-color: #ffffff; 
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); 
  margin-top: 0.125rem; 
}
</style>




