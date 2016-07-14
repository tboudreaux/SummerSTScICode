from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.37925,21.674],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_164131.02+214026.4/sdB_SDSSJ910_164131.02+214026.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_164131.02+214026.4/sdB_SDSSJ910_164131.02+214026.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
