<template>
  <div>
    <modal-comentario/>

    <component :is="componenteAtual"/>
  </div>
</template>

<script>
import Fase01 from '../fase-01/fase-01'
import Fase02 from '../fase-02/fase-02'
import Fase03 from '../fase-03/fase-03'
import Fase04 from '../fase-04/fase-04'
import Fase05 from '../fase-05/fase-05'
import ModalComentario from '@/components/ModalComentario'

export default {
  name: 'Lista',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Fase01,
    Fase02,
    Fase03,
    Fase04,
    Fase05,
    ModalComentario
  },
  computed: {
    componenteAtual () {
      return new Map([
        ['fase-01', Fase01],
        ['fase-02', Fase02],
        ['fase-03', Fase03],
        ['fase-04', Fase04],
        ['fase-05', Fase05]
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
