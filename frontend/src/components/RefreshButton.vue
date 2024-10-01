 
<template>
  <Button :label="label" @click="handleRefresh" :loading="isLoading">
    <template #icon>
      <FeatherIcon class="w-4" name="refresh-cw" />
    </template>
  </Button>
</template>
 
<script>
import { defineComponent } from 'vue'
import { FeatherIcon } from 'frappe-ui'
 
export default defineComponent({
  name: 'RefreshButton',
  components: {
    FeatherIcon
  },
  props: {
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    label() {
      return 'Refresh'
    }
  },
  methods: {
    handleRefresh() {
      this.$emit('refresh')
    }
  }
})
</script>
 
<style scoped>
 
</style>
 
 
 