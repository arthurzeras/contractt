<template>
  <div id="app" class="container-fluid">
    <layout-header/>

    <div class="row">
      <div class="col-2">
        <layout-sidebar/>
      </div>

      <div class="col">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import LayoutHeader from '@/components/Layout/LayoutHeader'
import LayoutSidebar from '@/components/Layout/LayoutSidebar'

export default {
  components: {
    LayoutHeader,
    LayoutSidebar
  }
}
</script>

<style lang="scss">

</style>
