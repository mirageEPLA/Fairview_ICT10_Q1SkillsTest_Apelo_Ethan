def create_order(event=None):

    coffees = document.querySelectorAll(".coffee")

    subtotal = 0
    items = ""

    # Get the selected coffee items
    for coffee in coffees:

        if coffee.checked:

            name = coffee.getAttribute("data-name")
            price = float(coffee.getAttribute("data-price"))

            subtotal += price

            items += f"""
            <p>
                {name}: ₱{price:.2f}
            </p>
            """


    # If no item is selected
    if subtotal == 0:

        document.querySelector("#receiptItems").innerHTML = \
            "<p>Please select at least one item.</p>"

        document.querySelector("#subtotal").innerText = "0.00"
        document.querySelector("#tax").innerText = "0.00"
        document.querySelector("#total").innerText = "0.00"

    else:

        # Calculate tax
        tax = subtotal * TAX_RATE

        # Calculate total
        total = subtotal + tax

        # Put selected items in receipt
        document.querySelector("#receiptItems").innerHTML = items

        # Put prices in receipt
        document.querySelector("#subtotal").innerText = \
            f"{subtotal:.2f}"

        document.querySelector("#tax").innerText = \
            f"{tax:.2f}"

        document.querySelector("#total").innerText = \
            f"{total:.2f}"


    # SHOW THE POP-UP
    document.querySelector("#receiptPopup").style.display = "block"


def close_receipt(event=None):

    # Hide the receipt
    document.querySelector("#receiptPopup").style.display = "none"

    </script>

</body>
</html
