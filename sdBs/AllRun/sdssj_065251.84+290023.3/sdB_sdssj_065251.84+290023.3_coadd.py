from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[103.216,29.006472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_065251.84+290023.3/sdB_sdssj_065251.84+290023.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_065251.84+290023.3/sdB_sdssj_065251.84+290023.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
