import api
import cash_on_hand
import noExcept
import overheads
import profit_loss



def main():


        forex = api.api_function()
        overheads.overhead_function(forex)
        cash_on_hand.coh_function(forex)
        profit_loss.profit_loss_function(forex)

main()