% rebase('vneseni_podatki.tpl')
        
    <p>
        
        <br><div class="notification is-danger">
            <table class="table is-fullwidth" cellpadding="8pt" cellspacing="0" width="700pt" border="2">
                <tr>
                    <td colspan="3">
                        <i>NASLEDNJI CIKEL</i>
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <td class="has-text-centered"><b>Datum</b></td>
                    <td class="has-text-centered"><b>Še toliko dni</b></td>
                </tr>
                <tr>
                    <td><b><i>Menstruacija</i></b></td>
                    <td class="has-text-centered">{{m1}} - {{m2}}</td>
                    <td class="has-text-centered">{{m3}}</td>
                </tr>
                <tr>
                    <td><b><i>Ovulacija</i></b></td>
                    <td class="has-text-centered">{{o1}}</td>
                    <td class="has-text-centered">{{o2}}</td>
                </tr>
                <tr>
                    <td><b><i>Plodni dnevi</i></b></td>
                    <td class="has-text-centered">{{p1}} - {{o1}}</td>
                    <td class="has-text-centered">{{p2}}</td>
                </tr>
            </table>
        </div>
    </p>
    {{!base}}