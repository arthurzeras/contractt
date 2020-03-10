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
      return 'Fase01'
    }
  },
  data () {
    return {
      faseAtual: 'fase-01'
    }
  }
}
</script>

<style scoped>

</style>
