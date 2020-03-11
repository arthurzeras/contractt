<template>
  <div class=" pt-3 pb-3 vh-100">
    <div class="embed-responsive embed-responsive-16by9">
      <embed src="https://expoforest.com.br/wp-content/uploads/2017/05/exemplo.pdf">
    </div>
    <div class="text-center mt-4">
      <button class="btn btn-outline-danger mr-2" @click="$emit('finalizar', 'reprovar')">Reprovar</button>
      <button class="btn btn-success" @click="$emit('finalizar', 'aprovar')">Aprovar</button>
<!--      <button class="btn btn-outline-warning mr-2">Pendente</button>-->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Fase01'
}
</script>

<style scoped>
.embed-responsive {
  height: 65%;
}
</style>
