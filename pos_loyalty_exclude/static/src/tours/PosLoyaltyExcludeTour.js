/** @odoo-module **/

import {ProductScreen} from "point_of_sale.tour.ProductScreenTourMethods";
import {getSteps, startSteps} from "point_of_sale.tour.utils";
import Tour from "web_tour.tour";

startSteps();
ProductScreen.do.clickHomeCategory();
ProductScreen.do.confirmOpeningPopup();

ProductScreen.do.clickPartnerButton();
ProductScreen.do.clickCustomer("Mr Odoo");
ProductScreen.exec.addOrderline("Product Include Loyalty", "1.00", "100");
ProductScreen.check.totalAmountIs("90.00");
ProductScreen.exec.addOrderline("Product Exclude Loyalty", "1.00", "100");
ProductScreen.check.totalAmountIs("100.00");
// totalAmount = ProductIncludeLoyalty + ProductExcludeLoyalty
ProductScreen.check.totalAmountIs("190.00");

Tour.register("PosExcludeLoyaltyPromotion", {test: true, url: "/pos/web"}, getSteps());
