c_state_tax = .05
c_county_tax = .025

user_input = int(input("Enter the total monthly sales: "))

def monthly_sales(total_sales):
    c_state_tax = .05
    c_county_tax = .025
    
    state_tax = total_sales * c_state_tax
    cnty_tax = total_sales * c_county_tax
    total_tax = cnty_tax + state_tax

    ret_output = "The county sales tax is: " + str(cnty_tax) + "\n"
    ret_output = ret_output + "The state sales tax is: " + str(state_tax) + "\n"
    ret_output = ret_output + "The total tax is: " + str(total_tax)

    return(ret_output)

print(monthly_sales(user_input))