from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[206.438458,0.111556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_134545.23-000641.6/sdB_sdssj_134545.23-000641.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_134545.23-000641.6/sdB_sdssj_134545.23-000641.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()