from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[337.208333,39.3215],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_222850.00+391917.4/sdB_sdssj_222850.00+391917.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_222850.00+391917.4/sdB_sdssj_222850.00+391917.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
