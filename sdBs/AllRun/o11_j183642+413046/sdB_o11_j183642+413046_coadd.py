from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[279.176958,41.513058],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_o11_j183642+413046/sdB_o11_j183642+413046_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_o11_j183642+413046/sdB_o11_j183642+413046_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
