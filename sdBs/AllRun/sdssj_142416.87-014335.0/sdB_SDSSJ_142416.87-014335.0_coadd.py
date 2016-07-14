from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[216.070292,-1.726389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_142416.87-014335.0/sdB_SDSSJ_142416.87-014335.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_142416.87-014335.0/sdB_SDSSJ_142416.87-014335.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
