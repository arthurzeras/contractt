<template>
  <div class="p-3">
  </div>
</template>

<script>
export default {
  name: 'Fase04',
  computed: {
    candidato () {
      return this.$route.params.email
    }
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>

</style>
