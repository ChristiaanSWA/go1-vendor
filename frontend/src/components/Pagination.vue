<template>
    <div class="flex justify-between gap-2 border-t sm:px-5 px-3 py-2 -ml-5">
      <div class="flex space-x-1 rounded bg-gray-100 p-0.5 text-sm">
        <Button
          v-for="num in [5,20, 50, 100]"
          :key="num"
          :variant="'subtle'"
          theme="gray"
          size="sm"
          :label="String(num)"
          @click="setItemsPerPage(num)"
          :disabled="itemsPerPage === num"
          class="flex flex-1 justify-center gap-2 whitespace-nowrap rounded-[7px] px-3 py-[5px] leading-none transition-colors focus:outline-none"
        />
      </div>
      <div class="float-right inline-flex items-center justify-center gap-2 transition-colors focus:outline-none text-gray-800 bg-gray-100 hover:bg-gray-200 active:bg-gray-300 focus-visible:ring focus-visible:ring-gray-400 h-7 text-base px-2 rounded ml-[682px]">
        <Button
          @click="loadMoreItems"
          :variant="'subtle'"
          theme="gray"
          size="sm"
          label="Load More"
        >
          Load More
        </Button>
      </div>
      <div class="float-right text-gray-700">
        {{ paginatedRows.length }} of {{ rows.length }}
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, watch } from 'vue'
  import { Button } from 'frappe-ui'
  
  export default {
    components: {
      Button
    },
    props: {
      rows: {
        type: Array,
        required: true,
      },
    },
    emits: ['update:paginatedRows'],
    setup(props, { emit }) {
      const itemsPerPage = ref(15)
      const currentPage = ref(1)
  
      const paginatedRows = computed(() => {
        const start = (currentPage.value - 1) * itemsPerPage.value
        const end = start + itemsPerPage.value
        return props.rows.slice(start, end)
      })

      watch(paginatedRows, (newPaginatedRows) => {
        emit('update:paginatedRows', newPaginatedRows)
      })
  
      const setItemsPerPage = (num) => {
        itemsPerPage.value = num
        currentPage.value = 1
      }
      const loadMoreItems = () => {
        itemsPerPage.value += 20
        currentPage.value = 1
      }
  
      return {
        paginatedRows,
        setItemsPerPage,
        loadMoreItems
      }
    }
  }
  </script>
  