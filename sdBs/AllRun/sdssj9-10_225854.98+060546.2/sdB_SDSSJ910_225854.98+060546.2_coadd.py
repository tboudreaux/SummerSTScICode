from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[344.729083,6.096167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_225854.98+060546.2/sdB_SDSSJ910_225854.98+060546.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_225854.98+060546.2/sdB_SDSSJ910_225854.98+060546.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
