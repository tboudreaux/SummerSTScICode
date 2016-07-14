from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[14.963167,0.272139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_005951.16-001619.7/sdB_sdssj_005951.16-001619.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_005951.16-001619.7/sdB_sdssj_005951.16-001619.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
