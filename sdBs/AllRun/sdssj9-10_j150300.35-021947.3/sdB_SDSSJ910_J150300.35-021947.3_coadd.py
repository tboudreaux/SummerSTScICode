from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[225.751458,-2.329806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_J150300.35-021947.3/sdB_SDSSJ910_J150300.35-021947.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_J150300.35-021947.3/sdB_SDSSJ910_J150300.35-021947.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
