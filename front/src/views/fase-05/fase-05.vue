<template>
  <div class="pt-3 pb-3">
    <ul>
      <li>Não negocia salário</li>
      <li>Disponibilidade para viajar</li>
      <li>Disponibilidade em horário comercial</li>
    </ul>

    <div class="text-center mt-2">
      <button class="btn btn-outline-danger mr-2" @click="$emit('finalizar', 'reprovar')">Recusada</button>
      <button class="btn btn-success" @click="$emit('finalizar', 'aprovar')">Aceita</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Fase05'
}
</script>

<style scoped>

</style>
