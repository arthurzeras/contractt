<template>
  <div class="p-3 vh-100">
    <h1>{{ candidato }}</h1>
    <div class="embed-responsive embed-responsive-16by9 h-75">
      <embed src="https://expoforest.com.br/wp-content/uploads/2017/05/exemplo.pdf">
    </div>
    <div class="text-center mt-2">
      <button class="btn btn-outline-danger mr-2" @click="$emit('finalizar', 'reprovar')">Reprovar</button>
      <button class="btn btn-success" @click="$emit('finalizar', 'aprovar')">Aprovar</button>
<!--      <button class="btn btn-outline-warning mr-2">Pendente</button>-->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Fase01',
  computed: {
    candidato () {
      return this.$route.params.email
    }
  }
}
</script>

<style scoped>

</style>
