from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.978167,0.391944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_152354.76+002331.0/sdB_SDSSJ910_152354.76+002331.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_152354.76+002331.0/sdB_SDSSJ910_152354.76+002331.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
