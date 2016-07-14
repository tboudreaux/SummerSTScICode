from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[259.77375,38.334222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_171905.70+382003.2/sdB_SDSSJ910_171905.70+382003.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_171905.70+382003.2/sdB_SDSSJ910_171905.70+382003.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
