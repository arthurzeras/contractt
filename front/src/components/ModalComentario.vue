<template>
  <div class="modal-comentario">
    <div class="modal fade show" style="display: block" tabindex="-1" v-if="visible">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Comentários e observações</h5>
            <button type="button" class="close" @click="hide()">
              <span>&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <textarea v-model="comentario" rows="10" class="form-control"/>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="hide()">Fechar</button>
            <button type="button" class="btn btn-primary" @click="ok()">Confirmar</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal-backdrop fade show" v-if="visible"></div>
  </div>
</template>

<script>
export default {
  data: () => ({
    visible: false,
    comentario: ''
  }),

  created () {
    this.$root.$on('comentario::show', this.show)
    this.$root.$on('comentario::hide', this.hide)
  },

  methods: {
    show () {
      this.visible = true
    },

    hide () {
      this.comentario = ''
      this.visible = false
    },

    ok () {
      this.$emit('ok', this.comentario)
    }
  }
}
</script>
