<template>
  <div>
    <modal-comentario @ok="handleModalOk"/>

    <component
      :is="componenteAtual"
      @finalizar="abrirModalComentario"
    />
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
      modalAcao: null,
      faseAtual: this.$route.query.fase
    }
  },
  methods: {
    abrirModalComentario (acao) {
      this.modalAcao = acao
      this.$root.$emit('comentario::show')
    },

    handleModalOk (comentario) {
      console.log(`enviar request para api com a ação de: ${this.modalAcao} e o comentario: ${comentario}`)
      this.$root.$emit('comentario::hide')
    }
  }
}
</script>

<style scoped>

</style>
