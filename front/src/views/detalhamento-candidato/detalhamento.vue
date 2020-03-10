<template>
  <div>
    <component :is="componenteAtual">
    </component>
  </div>
</template>

<script>
import Fase01 from '../fase-01/fase-01'
import Fase02 from '../fase-02/fase-02'

export default {
  name: 'Lista',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Fase01,
    Fase02
  },
  computed: {
    componenteAtual () {
      return new Map([
        ['fase-01', Fase01],
        ['fase-02', Fase02]
      ]).get(this.faseAtual)
    }
  },
  data () {
    return {
      faseAtual: this.$route.query.fase
    }
  }
}
</script>

<style scoped>

</style>
