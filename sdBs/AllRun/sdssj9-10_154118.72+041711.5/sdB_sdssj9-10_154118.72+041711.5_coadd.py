from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.328,4.286528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_154118.72+041711.5/sdB_sdssj9-10_154118.72+041711.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_154118.72+041711.5/sdB_sdssj9-10_154118.72+041711.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
