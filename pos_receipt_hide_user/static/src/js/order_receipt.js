odoo.define("pos_receipt_hide_user.OrderReceipt", function (require) {
  "use strict";

  const OrderReceipt = require("point_of_sale.OrderReceipt");
  const Registries = require("point_of_sale.Registries");

  const HideUserOrderReceipt = (OriginalOrderReceipt) =>
    class extends OriginalOrderReceipt {
      constructor({ hideUserState }) {
        super(...arguments);
        this.hideUserState = hideUserState;
        this.hide_option_from_config = this.env.pos.config.hide_user_option;
      }
      get userHidden() {
 
        return this.hideUserState.userHidden;
      }

      get HideUserOption() {
        return this.hide_option_from_config;
      }

      GetTrig(name) {
        const split_name = name.trim().split(/\s+/);

        if (split_name === 0) return '';

        const firstWord = split_name[0];
        const firstLetters = firstWord.slice(0,1);

        const lastWords = split_name[split_name.length -1];

        const lastLetters =lastWords.length > 1 ? lastWords.slice(0,2) : lastWords;

        return lastLetters + firstLetters;
      }


      get UserTrigram() {
        if (!this.env.pos.get_cashier()) {
          return ''
        }
        return this.GetTrig(this.env.pos.get_cashier().name);
      }


    };
  Registries.Component.extend(OrderReceipt, HideUserOrderReceipt);
  return OrderReceipt;
});
