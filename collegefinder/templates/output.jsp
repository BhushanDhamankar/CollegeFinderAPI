{% extends 'base.html' %}
{% block title %}output{% endblock %}
{% block aboutactive %}<li>{% endblock %}
{% block contactactive %}<li>{% endblock %}
{% block body %}

		<div class="inner">
			<div class="row">
				<div class="col-lg-12">
					<h1 class="page-header">College Finder</h1>
				</div>
			</div>
			<div class="row">

				<div class="col-lg-12">
					<div class="panel panel-default">
						<div class="panel-heading">
							Information :<br> Rank :
							{{r}}
							<br> Branch :
							{{b.name}}
							<br> Category :
							{{c.name}}
						</div>
						<div class="panel-body">
							<div class="row">
								<div class="card-body">
							
								{% if l %}

									<table class="table table-bordered table-striped">
										<thead>
											<tr>
												<th style="text-align: center">Sr. no.</th>
												<th style="text-align: center">Code</th>
												<th style="text-align: center">Name</th>
												<th style="text-align: center">Address</th>
												<th style="text-align: center">Rank</th>
											</tr>
										</thead>
										<tbody>

						
										
											{% for x in obj %}

												<tr>
													<td align="center">{{ x.1 }}</td>
													
													
													

													<td align="center">{{x.0.collegeid.code}}</td>
													<td align="center">{{x.0.collegeid.name}}</td>
													<td align="center">{{x.0.collegeid.address}}</td>
													<td align="center">{{x.0.rank}}</td>




													
												</tr>

										
											{% endfor %}
											
												
												
											
								{% else %}
									<div class="alert alert-dark" role="alert">
										<td align="center"><a href="#" class="alert-link">Result not found</a></td>
									</div>
								{% endif %}
							
										</tbody>
									</table>
								
								</div>

							</div>
						</div>
					</div>
				</div>
			</div>


		</div>




	</div>
{% endblock %}