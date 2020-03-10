<template>
  <div>
    <modal-comentario/>

    <component :is="componenteAtual"/>
  </div>
</template>

<script>
import Fase01 from '../fase-01/fase-01'
import Fase02 from '../fase-02/fase-02'
import ModalComentario from '@/components/ModalComentario'

export default {
  name: 'Lista',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Fase01,
    Fase02,
    ModalComentario
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
