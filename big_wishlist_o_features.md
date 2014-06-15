###Budgets
####Features
- Budgets can be any valid search
- Nested budgets
 - Leaves contain rules, non-leaves sum all leaves
- Detect conflicting budgets

####Notes
- Budget graphs/bars/whatever should show relative sizes of budgets (i.e. a $200 bar shouldn't be the same length as a $100 bar)

<br>
###Transactions
- Flexible schema- change it whenever you want
- Types of fields (not all may be necessary):
 - date (1 required)
 - dollar amount (1 required)
 - number
 - exclusive label ("category") (nested)
 - nonexclusive label ("tag") (nested)
 - free-form single-line text
 - free-form multiline text

<br>
###Transaction Processing
- New transactions go into "inbox"
- Transactions move into the main set once they've been processed (tagged, named, etc.)
 - Interface for processing transactions should be VERY easy, such that you can do a few when you've got spare time
- Filters for some automatic processing
 - Option to try automatic filtering but still require human approval
- Eventually, machine learning for automatic processing
- Option to notify another user to process a transaction (e.g. "What's this?")

<br>
###Reports/Visualization
- Flexible graph tools

<br>
###Accounts
- Multi-account, with permissions

<br>
###API
- bulk csv/json uploader for modifying transactions (with id matching)
- /api/transactions (Not sure if all of these are necessary or how they should work)
 - GET: input- query, output- list of transactions
 - PUT: input- bulk upload edit?
 - POST: input- list of transactions
 - DELETE: input- list of transactions
- /api/transactions/\<transaction-id\>
 - GET: output- single transaction
 - PUT: input- single modified transaction
 - POST: input- single new transaction
 - DELETE:
- [this guide](http://en.wikipedia.org/wiki/Representational_State_Transfer#Applied_to_web_services) disagrees with some of these

<br>
###Misc. Features
- Reimbursable matching
- OneReceipt integration
- mobile app
- in-browser script interpreter (for batch jobs)
 - sandboxing is very difficult
- way of identifying savings (i.e. look at balance, strip out cyclic part, see if there's enough that's not "promised" to something else) - answers "can I afford this"
- maintenance task scheduler that takes advantage of unused quota at EOD
