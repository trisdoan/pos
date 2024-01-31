odoo.define("pos_receipt_hide_user.ReceiptScreen", function (require) {
  "use strict";

  const {useState} = owl;
  const ReceiptScreen = require("point_of_sale.ReceiptScreen");
  const Registries = require("point_of_sale.Registries");

  const HideUserReceiptScreen = (OriginalReceiptScreen) =>
    class extends OriginalReceiptScreen {
      constructor() {
        super(...arguments);
        this.hideUserState = useState({userHidden: false});
      }

      hideUser() {
        this.hideUserState.userHidden = !this.hideUserState.userHidden;
      }

      get userHidden() {
        return this.hideUserState.userHidden;
      }
    };

  Registries.Component.extend(ReceiptScreen, HideUserReceiptScreen);
  return ReceiptScreen;
});
