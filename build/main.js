const catId= 'nhjr.timestamp';
const {api, type, Extension}= self.ClipCCExtension;
module.exports= class E extends Extension {
    onInit() {
      api.addCategory({ categoryId: catId, messageId: catId, color: '#5CB1D6' });
      api.addBlock({
          function: ()=> Date.now(),
          type: type.BlockType.REPORTER,
          opcode: catId + '.timestamp',
          messageId: catId + '.timestamp',
          categoryId: catId
      })
    }
    onUninit() { api.removeCategory(catId) }
}