<template>
  <div class="p-3">
    <p>
      <a
        href="https://portal.instruct.com.br/doku.php/instruct:pessoal:contratacao:frontend"
        target="_blank"
      >
        Link da entrevista comportamental no Survey Monkey
      </a>
    </p>

    <div class="text-center mt-2">
      <button class="btn btn-outline-danger mr-2" @click="$emit('finalizar', 'reprovar')">Reprovar</button>
      <button class="btn btn-success" @click="$emit('finalizar', 'aprovar')">Aprovar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Fase04'
}
</script>

<style scoped>

</style>
