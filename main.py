import api
import coh
import noExcept
import overheads
import profit_loss



def main():


        forex = api.api_function()
        overheads.overhead_function(forex)
        coh.coh_function(forex)
        profit_loss.profitloss_function(forex)

main()