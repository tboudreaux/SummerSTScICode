from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[126.859083,51.257472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_082726.18+511526.9/sdB_SDSSJ910_082726.18+511526.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_082726.18+511526.9/sdB_SDSSJ910_082726.18+511526.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
