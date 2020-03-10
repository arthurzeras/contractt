<template>
  <div class="p-3">
    <h1>Proposta</h1>
    <hr>
    <p>{{ candidato }}</p>

    <div class="text-center mt-2">
      <button class="btn btn-outline-danger mr-2">Recusada</button>
      <button class="btn btn-success">Aceita</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Fase05',
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
