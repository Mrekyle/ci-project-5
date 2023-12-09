
// Handling the increment and decrement of the items quantity in the store application 

/**
 * Disables the +/- Buttons outside the range limits.
 */
function enableDisable(itemId) {
    let currentVal = parseInt($('#id_qty_${itemId}').val());
    let minDisabled = currentVal < 2;
    let maxDisabled = currentVal > 98;


    $(`#decrement-qty_${itemId}`).prop('disabled', minDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', maxDisabled);
}

/**
 * Ensures buttons are re-enabled/disabled on page reload
 */
let allInputs = $('.qty_input');
for(var i = 0; i < allInputs.length; i++){
    let itemId = $(allInputs[i]).data('item_id')
    enableDisable(itemId)
}

/**
 * Checks the quantity and the buttons each time the input has been changed
 */
$('.qty_input').change(function() {
    let itemId = $(this).data('item_id');
    enableDisable(itemId);
})

/**
 * Checking the DOM tree for the next elements. Allowing the increment in the item quantity
 */
$('.increment-qty').click(function(e) {
    e.preventDefault();
    let closeInput = $(this).closest('input-group').find('.qty_input')[0];
    let currentVal = parseInt($(closeInput).val());
    $(closeInput).val(currentVal + 1)
    let itemId = $(this).data('item_id');
    enableDisable(itemId);
})

/**
 * Checking the DOM tree for the next elements. Allowing the decrement in the item quantity
 */
$('.increment-qty').click(function(e) {
    e.preventDefault();
    let closeInput = $(this).closest('input-group').find('.qty_input')[0];
    let currentVal = parseInt($(closeInput).val());
    $(closeInput).val(currentVal - 1)
    let itemId = $(this).data('item_id');
    enableDisable(itemId);
})