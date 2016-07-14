from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.554542,16.519278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_163413.09+163109.4/sdB_sdssj9-10_163413.09+163109.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_163413.09+163109.4/sdB_sdssj9-10_163413.09+163109.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()