$(document).ready(function() {
    $('#team-form').on('submit', function(event) {
        event.preventDefault();
        console.log("Submitted");
        let team1 = $('#team1').val();
        let team2 = $('#team2').val();
        
        $.post('/find_matches', { team1: team1, team2: team2 }, function(matches) {
            let matchesByEvent = {};

            matches.forEach((match) => {
                let eventKey = match.event_key;
                if (!matchesByEvent[eventKey]) {
                    matchesByEvent[eventKey] = [];
                }
                matchesByEvent[eventKey].push(match);
            });

            let sortedEvents = Object.keys(matchesByEvent).sort();
            let cardContent = '';

            sortedEvents.forEach((eventKey) => {
                let eventMatches = matchesByEvent[eventKey];
                let year = eventKey.substring(0, 4);
                let eventAcronym = eventKey.substring(4);

                eventMatches.forEach((match) => {
                    let matchNumber = match.key.split('_')[1].toUpperCase();
                    cardContent += `
                        <div class="card mb-3">
                            <div class="card-header">
                                Match: ${matchNumber}, Event: ${eventAcronym.toUpperCase()} (${year})
                            </div>
                            <div class="card-body">
                                <p><strong>Match Key:</strong> ${match.key}</p>
                                <p><strong>Event Key:</strong> ${match.event_key}</p>
                                <p><strong>Match Type:</strong> ${match.comp_level.toUpperCase()}</p>
                                <p><strong>Red Alliance:</strong> ${match.alliances.red.team_keys.join(', ')}</p>
                                <p><strong>Blue Alliance:</strong> ${match.alliances.blue.team_keys.join(', ')}</p>
                            </div>
                        </div>`;
                });
            });

            $('#matches-accordion').html(cardContent);
        }).fail(function() {
            $('#matches-accordion').html('<div class="alert alert-danger" role="alert">Error fetching matches. Please try again.</div>');
        });
    });
});
