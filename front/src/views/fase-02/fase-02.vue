<template>
  <div class="pt-3 pb-3">
    <p>
      <a
        href="https://pt.surveymonkey.com/analyze/mjkWTttSw38qXIoa26BwDOPm569P2I3HdUvSojr5ih4_3D?tab_clicked=1"
        target="_blank"
      >
        Link do survey monkey
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
  name: 'Fase02'
}
</script>

<style scoped>

</style>
