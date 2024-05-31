import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Analytical Report", page_icon="📊")

st.markdown("# Analytical Report")

st.write(
    """
    Here you can find the tableau public workbook where I analyze some of my data. 
    Feel free to explore the different dashboards at your own pace and play around with the filters.      
    """)

html_temp="""
<div class='tableauPlaceholder' id='viz1717144888771' style='position: relative'><noscript><a href='#'><img alt=' ' 
src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;On&#47;Online_courses_Project&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a>
</noscript><object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> 
<param name='site_root' value='' />
<param name='name' value='Online_courses_Project&#47;Dashboard1' />
<param name='tabs' value='yes' /><param name='toolbar' value='yes' />
<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;On&#47;Online_courses_Project&#47;Dashboard1&#47;1.png' /> 
<param name='animate_transition' value='yes' />
<param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' />
<param name='display_overlay' value='yes' />
<param name='display_count' value='yes' />
<param name='language' value='fr-FR' />
<param name='filter' value='publish=yes' />
</object></div>                
<script type='text/javascript'>                    
var divElement = document.getElementById('viz1717144888771');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1100px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='750px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} 
else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1100px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='750px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} 
else { vizElement.style.width='100%';vizElement.style.minHeight='1950px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>
"""

components.html(html_temp, width=1100, height=750)

st.write("# Short summary")

st.write(
    """
    Dashboard 1:
    - The most popular courses are the ones offering a beginner/all level of accessibility. Reducing the amount of prior knowledge necessary to follow a course allows a larger population of students to be interested in them.
    - The higher the rating is, the more students are enrolled in a course. While this can mean that one of the factors influencing a student's choice to enroll in a course is its rating, 
    this metric can be highly influence by the number of students enrolled in a course. A course that was just published with very few students will be more influence by outliers than a well established course.
    - Looking at the most popular courses overall, we can see that a majority of them is related to 'Development' (Web Development).
    - Looking at the evolution in the number of students enrolled in each Subject, there is a trend with students massively enrolling into courses related to Web Development compared to other subjects.

    Dashboard 2:
    - Looking at the factors influencing the pricing of courses. 
        - While there is a positive correlation between prices and length of the courses, it is not as accentuated as expected. Some short courses can be priced the same or even higher than longer ones (particularly if you look at Udemy's data). 
        - There's a difference in the prices range and distribution between the two academies. edX does seem to charge higher prices overall compare to Udemy.
        - Aside from the academies, the factor that influences the prices the most is the level of the course.
    - Supposing that Udemy has a similar working process as IronHack, I thought that the more number of lessons the more reviews would be posted for a course. 
    But it appears that unlike Ironhack Udemy does not ask for student's reviews about a course's lessons on a regulary basis. They are more focused on collecting reviews during the first lessons than on the overall course. 
    This leads to a higher number of reviews in a shorter course compare to a longer one that has the same amount of students.
    - Looking at the time since creation of a course, I supposed that the longer a course was established the more total students they would have. But it seems that this hypothesis is false and other factors like the subject and how up to date a course is have more influence on this.
    """)

st.write("""If you're still interested in knowing more about online courses...
         how about trying to use the prediction model and predict how many students there will be in a course in 4 years?""")