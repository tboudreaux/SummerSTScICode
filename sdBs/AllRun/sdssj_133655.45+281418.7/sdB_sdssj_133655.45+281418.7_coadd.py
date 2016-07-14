from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[204.231042,28.238528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_133655.45+281418.7/sdB_sdssj_133655.45+281418.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_133655.45+281418.7/sdB_sdssj_133655.45+281418.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
