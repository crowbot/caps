# caps

# Install

Clone the repository

```
git clone git@github.com:mysociety/caps.git
cd caps
cp conf/config.py-example conf/config.py
```

A Vagrantfile is included for local development. Assuming you have [Vagrant](https://www.vagrantup.com/) installed, you can create a Vagrant VM with:

```
vagrant up
```

Then SSH into the VM, and run the server script:

```
vagrant ssh
script/server
```

The site will be visible at <http://localhost:8000>.

# Get and preprocess data (includes setting up a Solr text index for the plan document text)

```
script/update
```

The Solr server interface will be visible at <http://localhost:8983>

# Get and load emissions data

```
script/manage import_emissions_data
```

