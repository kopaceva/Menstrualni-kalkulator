% import model
% import vmesnik
% import datetime
% import calendar
% rebase('datumska_stran.tpl')
        
        <p>
            
            <br><div class="notification is-danger">
                <table class="table is-fullwidth" cellpadding="8pt" cellspacing="0" width="700pt" border="2">
                    <tr>
                        <td colspan="2">
                            <i>ZAMUDA MENSTRUACIJE</i>
                        </td>
                    </tr>
                    <tr>
                        <td class="has-text-centered"><b>Predviden začetek menstruacije</b></td>
                        <td class="has-text-centered"><b>Zamuja toliko dni</b></td>
                    </tr>
                    <tr>
                        <td class="has-text-centered">{{z1}}</td>
                        <td class="has-text-centered">{{z2}}</td>
                    </tr>
                </table>
            </div>

            <br> 
            <div class="content">
                <ul><b>Možni vzroki za zamujanje:</b>
                    <li> stres,
                    <li> preveč športne aktivnosti,
                    <li> neredno spanje,
                    <li> hitra sprememba telesne teže,
                    <li> reakcija na zdravila,
                    <li> nosečnost.
                </ul>
            </div>
        </p>