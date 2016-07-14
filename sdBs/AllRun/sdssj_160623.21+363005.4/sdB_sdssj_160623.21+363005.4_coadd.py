from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.596708,36.5015],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_160623.21+363005.4/sdB_sdssj_160623.21+363005.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_160623.21+363005.4/sdB_sdssj_160623.21+363005.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()